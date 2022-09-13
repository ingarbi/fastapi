"""add content to table

Revision ID: 84fd9d12c217
Revises: e9efe9f28fb5
Create Date: 2022-09-13 11:25:51.501082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84fd9d12c217'
down_revision = 'e9efe9f28fb5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
