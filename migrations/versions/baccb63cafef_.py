"""empty message

Revision ID: baccb63cafef
Revises: 
Create Date: 2021-04-10 19:11:29.215390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baccb63cafef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=95), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('bedroom', sa.String(length=30), nullable=True),
    sa.Column('bathroom', sa.String(length=30), nullable=True),
    sa.Column('price', sa.String(length=100), nullable=True),
    sa.Column('ptype', sa.String(length=25), nullable=True),
    sa.Column('location', sa.String(length=300), nullable=True),
    sa.Column('photo', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
