"""create post table

Revision ID: e9efe9f28fb5
Revises: 
Create Date: 2022-09-13 10:13:50.263037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9efe9f28fb5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(),  nullable=False))


def downgrade():
    op.drop_table('posts')
