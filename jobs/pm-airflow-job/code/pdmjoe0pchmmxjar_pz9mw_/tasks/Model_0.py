from pdmjoe0pchmmxjar_pz9mw_.utils import *

def Model_0():
    from datetime import timedelta
    from airflow.operators.bash import BashOperator
    dbt_props_cmd = ""

    if "run_profile":
        dbt_props_cmd = " --profile run_profile"

    return BashOperator(
        task_id = "Model_0",
        bash_command = f'''$PROPHECY_HOME/run_dbt.sh "{"; ".join(["dbt run" + dbt_props_cmd, "dbt test" + dbt_props_cmd])}"''',
        env = {
          "DBT_PROFILE_SECRET": "44cVxoi8MXgUyuQ34qFZZ", 
          "GIT_TOKEN_SECRET": "Gn3AwQ5vSW1jqmT40pe_Q_", 
          "GIT_ENTITY": "branch", 
          "GIT_ENTITY_VALUE": "dev", 
          "GIT_SSH_URL": "https://github.com/poojaSprophecy/snowflake-demo", 
          "GIT_SUB_PATH": ""
        },
        append_env = True,
    )
