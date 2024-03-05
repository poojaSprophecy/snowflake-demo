from aawqaml_fdxtafbo3lux7a_.utils import *

def DBT_0():
    from datetime import timedelta
    from airflow.operators.bash import BashOperator
    dbt_props_cmd = ""

    if "run_profile":
        dbt_props_cmd = " --profile run_profile"

    return BashOperator(
        task_id = "DBT_0",
        bash_command = f'''$PROPHECY_HOME/run_dbt.sh "{"; ".join(["dbt run" + dbt_props_cmd, "dbt test" + dbt_props_cmd])}"''',
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
