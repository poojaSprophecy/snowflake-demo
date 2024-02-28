def DBT_0():
    from datetime import timedelta
    from airflow.operators.bash import BashOperator

    return BashOperator(
        task_id = "DBT_0",
        bash_command = "set -euxo pipefail; tmpDir=`mktemp -d`; git clone https://github.com/poojaSprophecy/snowflake-demo --branch main --single-branch $tmpDir; cd $tmpDir/; dbt run --profile run_profile_snowflake; dbt test --profile run_profile_snowflake; ",
        env = {"DBT_PROFILES_DIR" : "/home/airflow/gcs/data"},
        append_env = True,
    )
