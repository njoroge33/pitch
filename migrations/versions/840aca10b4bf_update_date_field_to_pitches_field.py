"""update date field to pitches field

Revision ID: 840aca10b4bf
Revises: 17f3503b0364
Create Date: 2019-11-26 16:17:27.139371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '840aca10b4bf'
down_revision = '17f3503b0364'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pitches', 'category',
               existing_type=sa.VARCHAR(length=9),
               nullable=True,
               existing_server_default=sa.text("'product'::character varying"))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pitches', 'category',
               existing_type=sa.VARCHAR(length=9),
               nullable=False,
               existing_server_default=sa.text("'product'::character varying"))
    # ### end Alembic commands ###
