# Enterprise DataOps & MLOps Platform

Production-grade DataOps platform automating CI/CD, data quality, feature management, and MLOps across multi-environment deployments. Built with Terraform, GitHub Actions, dbt, Great Expectations, MLflow, and Apache Airflow.

## Architecture
 [GitHub Repositories]
        ↓
 [GitHub Actions: CI/CD]
        ↓
 [Dev → Staging → Prod]
        ↓
[Terraform: Multi-Cloud Infrastructure]
        ↓
[Azure DevOps / GitHub Environments]
        ↓
[Data Quality Gates: Great Expectations]
        ↓
[dbt: Transformations & Tests]
        ↓
[MLflow: Feature Store & Model Registry]
        ↓
[Airflow: Orchestration & Monitoring]
        ↓
[Observability: Grafana + Prometheus]

## Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **IaC** | Terraform | Azure + AWS infrastructure as code |
| **CI/CD** | GitHub Actions | Automated testing, deployment, rollback |
| **Data Quality** | Great Expectations, dbt tests | Validation, anomaly detection, contracts |
| **Transform** | dbt Core + Cloud | SQL models, documentation, lineage |
| **Feature Store** | Feast + MLflow | ML feature management and serving |
| **MLOps** | MLflow, Docker, Kubernetes | Model training, deployment, monitoring |
| **Orchestration** | Apache Airflow | Pipeline scheduling and dependency mgmt |
| **Monitoring** | Grafana, Prometheus, PagerDuty | Observability and alerting |
| **Containers** | Docker, Kubernetes | Scalable workload execution |

## Key Features

### 🔄 CI/CD for Data Pipelines
- **Automated Testing**: Every PR triggers dbt tests, Great Expectations suites, and Python unit tests
- **Environment Promotion**: Dev → Staging → Prod with Terraform workspace separation
- **Rollback**: Automatic rollback on failed deployments with state file versioning
- **Secrets Management**: Azure Key Vault + AWS Secrets Manager integration

### ✅ Data Quality & Contracts
- **Great Expectations**: 50+ expectations per table covering nulls, ranges, referential integrity
- **dbt Tests**: Schema, uniqueness, and relationship tests on all models
- **Data Contracts**: JSON schema enforcement between producers and consumers
- **Lineage**: dbt docs + DataHub integration for column-level lineage

### 🤖 MLOps & Feature Store
- **Feature Engineering**: Feast feature definitions versioned with Git
- **Model Registry**: MLflow tracks experiments, versions, and stage transitions
- **A/B Testing**: Shadow deployment and traffic splitting for model variants
- **Drift Detection**: Automated data drift and model performance monitoring

## Project Structure
enterprise-dataops-mlops-platform/
├── .github/
│   └── workflows/
│       ├── ci-cd.yml
│       ├── data-quality.yml
│       └── mlops-deploy.yml
├── infrastructure/
│   ├── terraform/
│   │   ├── modules/
│   │   │   ├── azure_data_platform/
│   │   │   └── aws_data_platform/
│   │   ├── environments/
│   │   │   ├── dev/
│   │   │   ├── staging/
│   │   │   └── prod/
│   │   └── main.tf
│   └── kubernetes/
│       └── airflow-deployment.yaml
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   ├── intermediate/
│   │   └── marts/
│   ├── tests/
│   └── macros/
├── data_quality/
│   ├── great_expectations/
│   │   ├── expectations/
│   │   └── checkpoints/
│   └── dbt_tests/
├── mlops/
│   ├── features/
│   │   └── feature_definitions.py
│   ├── training/
│   │   └── train_model.py
│   ├── serving/
│   │   └── model_server.py
│   └── monitoring/
│       └── drift_detector.py
├── airflow/
│   └── dags/
│       ├── data_pipeline_dag.py
│       └── ml_pipeline_dag.py
├── docs/
│   ├── dataops_playbook.md
│   └── mlops_guide.md
└── README.md

## DataOps Workflow

1. **Developer commits** to feature branch
2. **GitHub Actions** runs linting, unit tests, dbt compile
3. **Great Expectations** validates sample data against production schema
4. **Terraform plan** previews infrastructure changes
5. **Staging deployment** runs full integration tests
6. **Manual approval** gates production promotion
7. **Terraform apply** deploys to production with blue/green strategy
8. **Airflow** automatically picks up new DAG versions
9. **Monitoring** alerts on anomalies, failures, or SLA breaches

## MLOps Workflow

1. **Feature engineering** pipeline runs via Airflow
2. **Feast** materializes features to online/offline stores
3. **Training pipeline** logs experiments to MLflow
4. **Model validation** against holdout dataset
5. **Model registration** to MLflow Model Registry (Staging)
6. **A/B test** deployment to 10% traffic
7. **Performance monitoring** tracks inference latency and accuracy
8. **Full promotion** to Production after validation period

## Quick Start

```bash
# 1. Clone and setup
git clone https://github.com/todimaajay1/enterprise-dataops-mlops-platform.git
cd enterprise-dataops-mlops-platform
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 2. Deploy dev environment
cd infrastructure/terraform/environments/dev
terraform init && terraform apply

# 3. Run data quality suite
cd data_quality/great_expectations
great_expectations checkpoint run prod_checkpoint

# 4. Run dbt models
cd dbt
dbt run --target dev && dbt test

# 5. Start Airflow
docker-compose -f infrastructure/kubernetes/airflow-deployment.yaml up -d

# 6. Register features
cd mlops/features
python feature_definitions.py apply

Compliance & Governance
SOC-2: All changes tracked, tested, and approved
HIPAA: PHI environments isolated with encryption and audit logging
GDPR: Data retention policies automated via Terraform
Audit Trail: Complete lineage from source to model prediction

License
Enterprise DataOps reference architecture. MIT License.

