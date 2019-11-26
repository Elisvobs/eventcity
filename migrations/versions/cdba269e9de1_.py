"""empty message

Revision ID: cdba269e9de1
Revises: 5d4abe45c6d9
Create Date: 2016-06-21 11:09:54.239439

"""

# revision identifiers, used by Alembic.
revision = 'cdba269e9de1'
down_revision = '5d4abe45c6d9'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mails', sa.Column('subject', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mails', 'subject')
    ### end Alembic commands ###
