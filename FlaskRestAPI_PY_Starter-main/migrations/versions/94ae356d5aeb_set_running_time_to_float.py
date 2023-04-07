"""set running time to float

Revision ID: 94ae356d5aeb
Revises: a793192640c6
Create Date: 2023-04-05 15:20:21.972072

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '94ae356d5aeb'
down_revision = 'a793192640c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.alter_column('running_time',
               existing_type=mysql.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('song', schema=None) as batch_op:
        batch_op.alter_column('running_time',
               existing_type=sa.Float(),
               type_=mysql.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###