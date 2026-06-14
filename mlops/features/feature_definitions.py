"""
Feast feature definitions for the enterprise feature store.
Manages online and offline features for ML model training and serving.
"""
from feast import Entity, Feature, FeatureView, ValueType, FileSource
from feast.types import Float32, Int64, String, Bool
from datetime import timedelta

# Define entities
patient = Entity(
    name="patient_id",
    value_type=ValueType.STRING,
    description="Unique patient identifier"
)

# Define feature sources
patient_features_source = FileSource(
    path="data/gold/patient_features.parquet",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp"
)

# Feature view for patient risk features
patient_risk_features = FeatureView(
    name="patient_risk_features",
    entities=["patient_id"],
    ttl=timedelta(days=365),
    features=[
        Feature(name="age", dtype=Int64),
        Feature(name="avg_observation_value", dtype=Float32),
        Feature(name="num_encounters_30d", dtype=Int64),
        Feature(name="risk_stratification", dtype=String),
        Feature(name="has_chronic_condition", dtype=Bool),
        Feature(name="last_readmission_days", dtype=Int64),
    ],
    online=True,
    source=patient_features_source,
    tags={"team": "data-science", "domain": "healthcare"}
)

# Feature view for real-time vitals
vitals_features = FeatureView(
    name="real_time_vitals",
    entities=["patient_id"],
    ttl=timedelta(hours=1),
    features=[
        Feature(name="heart_rate", dtype=Float32),
        Feature(name="blood_pressure_systolic", dtype=Float32),
        Feature(name="blood_pressure_diastolic", dtype=Float32),
        Feature(name="temperature", dtype=Float32),
        Feature(name="oxygen_saturation", dtype=Float32),
    ],
    online=True,
    source=FileSource(
        path="data/gold/vitals_stream.parquet",
        event_timestamp_column="event_timestamp"
    ),
    tags={"team": "clinical-ai", "domain": "healthcare", "freshness": "realtime"}
)

def apply_features():
    """Apply feature definitions to Feast feature store."""
    from feast import FeatureStore
    store = FeatureStore(repo_path=".")
    store.apply([patient, patient_risk_features, vitals_features])
    print("Feature definitions applied successfully.")

if __name__ == "__main__":
    apply_features()
