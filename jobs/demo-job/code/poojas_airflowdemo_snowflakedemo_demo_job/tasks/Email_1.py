from poojas_airflowdemo_snowflakedemo_demo_job.utils import *

def Email_1():
    from airflow.operators.email import EmailOperator
    from datetime import timedelta

    return EmailOperator(
        task_id = "Email_1",
        to = "poojas@prophecy.io",
        subject = "Starting job",
        html_content = "Stating job at {{execution_date}}",
        cc = None,
        bcc = None,
        mime_subtype = "mixed",
        mime_charset = "utf-8",
        conn_id = "email_default",
    )
