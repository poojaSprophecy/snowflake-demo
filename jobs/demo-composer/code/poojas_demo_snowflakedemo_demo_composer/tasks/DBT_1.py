from poojas_demo_snowflakedemo_demo_composer.utils import *

def DBT_1():
    from datetime import timedelta
    from airflow.operators.bash import BashOperator
    envs = {}
    dbt_props_cmd = ""

    if "/home/airflow/gcs/data":
        envs = {"DBT_PROFILES_DIR" : "/home/airflow/gcs/data"}

    if "run_profile_snowflake":
        dbt_props_cmd = " --profile run_profile_snowflake"

    return BashOperator(
        task_id = "DBT_1",
        bash_command = " && ".join(
          ["{} && cd $tmpDir/{}".format(
             (
               "set -euxo pipefail && tmpDir=`mktemp -d` && git clone "
               + "{} --branch {} --single-branch $tmpDir".format(
                 "https://github.com/poojaSprophecy/mrr-playbook",
                 "master"
               )
             ),
             ""
           ),            "dbt run" + dbt_props_cmd,  "dbt test" + dbt_props_cmd]
        ),
        env = envs,
        append_env = True,
    )
