"""empty message

Revision ID: 0aa2fa812248
Revises: ff2390fd38e2
Create Date: 2016-06-13 11:31:32.076870

"""

# revision identifiers, used by Alembic.
revision = '0aa2fa812248'
down_revision = 'ff2390fd38e2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False))
    ### end Alembic commands ###
