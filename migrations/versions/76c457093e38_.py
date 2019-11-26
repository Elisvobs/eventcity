"""empty message

Revision ID: 76c457093e38
Revises: bf3e8c2a01f6
Create Date: 2017-08-11 22:59:11.276589

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '76c457093e38'
down_revision = 'bf3e8c2a01f6'


def upgrade():
    # commands auto generated by Alembic - please adjust! #
    op.alter_column('speaker', 'photo', new_column_name='photo_url')
    op.alter_column('speaker', 'thumbnail', new_column_name='thumbnail_image_url')
    op.alter_column('speaker', 'small', new_column_name='small_image_url')
    op.alter_column('speaker', 'icon', new_column_name='icon_image_url')
    # end Alembic commands #


def downgrade():
    # commands auto generated by Alembic - please adjust! #
    op.alter_column('speaker', 'photo_url', new_column_name='photo')
    op.alter_column('speaker', 'thumbnail_image_url', new_column_name='thumbnail')
    op.alter_column('speaker', 'small_image_url', new_column_name='small')
    op.alter_column('speaker', 'icon_image_url', new_column_name='icon')
    # end Alembic commands #
