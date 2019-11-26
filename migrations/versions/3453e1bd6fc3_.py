"""empty message

Revision ID: 3453e1bd6fc3
Revises: 7cf31ed98b0c
Create Date: 2016-07-28 13:29:08.360087

"""

# revision identifiers, used by Alembic.
revision = '3453e1bd6fc3'
down_revision = '7cf31ed98b0c'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('paypal_email', sa.String(), nullable=True))
    op.add_column('events_version', sa.Column('paypal_email', sa.String(), autoincrement=False, nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'paypal_email')
    op.drop_column('events', 'paypal_email')
    ### end Alembic commands ###
