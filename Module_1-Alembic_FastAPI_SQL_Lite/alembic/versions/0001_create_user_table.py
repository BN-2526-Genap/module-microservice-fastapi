from alembic import op
import sqlalchemy as sa


revision = "0001_create_user_table"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("name", sa.String(length=100), index=True, nullable=False),
        sa.Column("email", sa.String(length=150), unique=True, index=True, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("user")

