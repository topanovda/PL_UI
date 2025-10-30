import os
from dotenv import load_dotenv

stages = {
    "dev" : "https://dev.po.ladcloud.ru",
    "staging" : "https://lk.staging.po.ladcloud.ru",
    "production" : "https://cloud.projectlad.ru"
}

class Links:
    STAGE = os.getenv("STAGE", "staging")
    HOST = stages.get(STAGE, stages["staging"])
    # HOST = stages[os.getenv("STAGE")]

    PROJECTS_PAGE = f"{HOST}/gant-v2"
    NSI_PAGE = f"{HOST}/nsi"
    ATTRIBUTE_PAGE = f"{HOST}/nsi/dir?nsi_id=LZ3r_ISmVYN040P0C59t7&nsi_type=attribute"
    FACT_PAGE = f"{HOST}/fact"
    REPORTS_PAGE = f"{HOST}/reports"
    DASHBOARD_PAGE = f"{HOST}/reports/dashboard"
    DATA_STORAGE_PAGE = f"{HOST}/data-storage"
