import pytest
from dbt.tests.adapter.dbt_clone.test_dbt_clone import (
    BaseClonePossible,
    BaseCloneSameSourceAndTarget,
    BaseCloneNotPossible,
)


class TestBigQueryClonePossible(BaseClonePossible):
    @pytest.fixture(autouse=True)
    def clean_up(self, project):
        yield
        with project.adapter.connection_named("__test"):
            relation = project.adapter.Relation.create(
                database=project.database, schema=f"{project.test_schema}_seeds"
            )
            project.adapter.drop_schema(relation)

            relation = project.adapter.Relation.create(
                database=project.database, schema=project.test_schema
            )
            project.adapter.drop_schema(relation)

    pass


class TestBigQueryCloneSameSourceAndTarget(BaseCloneSameSourceAndTarget):
    pass


class TestBigQueryCloneNotPossible(BaseCloneNotPossible):
    pass
