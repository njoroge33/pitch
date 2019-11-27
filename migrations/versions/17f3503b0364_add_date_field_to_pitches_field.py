"""add date field to pitches field

Revision ID: 17f3503b0364
Revises: a3b997d4473d
Create Date: 2019-11-26 15:45:48.638401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17f3503b0364'
down_revision = 'a3b997d4473d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('pitches', sa.Column('date', sa.DateTime(), nullable=False))


def downgrade():
    op.drop_column('pitches', 'date')
