def DBT_0():
    from datetime import timedelta
    from airflow.operators.bash import BashOperator

    return BashOperator(
        task_id = "DBT_0",
        bash_command = "$PROPHECY_HOME/run_dbt.sh \"dbt run --profile run_profile; dbt test --profile run_profile; \"",
        env = {
          "DBT_PROFILE_SECRET": "bVdWSDRsvCf7r6_iOGTiw", 
          "GIT_TOKEN_SECRET": "TFqbXnXxNHLOf6jPmvoZ1Q_", 
          "GIT_ENTITY": "branch", 
          "GIT_ENTITY_VALUE": "main", 
          "GIT_SSH_URL": "https://github.com/poojaSprophecy/snowflake-demo", 
          "GIT_SUB_PATH": ""
        },
        append_env = True,
    )
