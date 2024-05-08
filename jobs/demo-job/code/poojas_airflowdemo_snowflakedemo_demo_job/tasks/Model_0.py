from poojas_airflowdemo_snowflakedemo_demo_job.utils import *

def Model_0():
    from datetime import timedelta
    from airflow.operators.bash import BashOperator
    envs = {}
    dbt_props_cmd = ""

    if "/home/airflow/gcs/data":
        envs = {"DBT_PROFILES_DIR" : "/home/airflow/gcs/data"}

    if "run_profile_snowflake":
        dbt_props_cmd = " --profile run_profile_snowflake"

    return BashOperator(
        task_id = "Model_0",
        bash_command = " && ".join(
          ["{} && cd $tmpDir/{}".format(
             (
               "set -euxo pipefail && tmpDir=`mktemp -d` && git clone "
               + "{} --branch {} --single-branch $tmpDir".format(
                 "https://github.com/poojaSprophecy/snowflake-demo",
                 "dev"
               )
             ),
             ""
           ),            "dbt run" + dbt_props_cmd,  "dbt test" + dbt_props_cmd]
        ),
        env = envs,
        append_env = True,
    )