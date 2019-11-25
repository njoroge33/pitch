"""Add pitch model

Revision ID: a3b997d4473d
Revises: abe4bd546391
Create Date: 2019-11-25 22:56:35.657211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3b997d4473d'
down_revision = 'abe4bd546391'
branch_labels = None
depends_on = None


def upgrade():
    category_enum = [
        'product',
        'interview',
        'promotion'
    ]
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('category', sa.Enum(*category_enum, name='category_enum', native_enum=False), server_default='product', nullable=False),
    sa.Column('upvotes', sa.Integer(), nullable=True),
    sa.Column('downvotes', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pitches_description'), 'pitches', ['description'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pitches_description'), table_name='pitches')
    op.drop_table('pitches')
    # ### end Alembic commands ###
