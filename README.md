# db_alenusa
cd "C:\Users\ramirei3\OneDrive - Grupo Alen\Documents\Repositories\automation_scripts"

git clone https://github.com/iramirezalenusa/db_alenusa.git

python -m venv db_venv
.\db_venv\Scripts\Activate.ps1

# dbt install
pip install dbt-core dbt-postgres
pip install --upgrade mashumaro
dbt init

Welcome to your new dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test


### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
