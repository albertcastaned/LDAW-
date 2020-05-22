"""empty message

Revision ID: b0159e473c2f
Revises: d166abd9d023
Create Date: 2020-05-22 13:45:58.116697

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b0159e473c2f'
down_revision = 'd166abd9d023'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Ventas', schema=None) as batch_op:
        batch_op.drop_column('ticket')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Ventas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ticket', mysql.INTEGER(), server_default=sa.text("'1'"), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
