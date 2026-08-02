import os
import time
from prefect import flow, task

@task
def process_incoming_call(caller_id: str):
    print(f"در حال پردازش تماس از شماره: {caller_id}")
    return f"تماس {caller_id} پاسخ داده شد."

@flow(name="Main-AI-Agent-Orchestrator")
def main_agent_flow(caller_id: str = "Unknown"):
    print("رهبر ارکستر (Prefect) فعال شد...")
    result = process_incoming_call(caller_id)
    print(result)

if __name__ == "__main__":
    print("ایستگاه اجرا (Worker) به Prefect متصل شد.")
    main_agent_flow.serve(name="render-agent-runner")
