"""Initial Migration

Revision ID: d06b0384fac0
Revises: 
Create Date: 2020-06-26 23:11:15.175214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd06b0384fac0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('phoneno', sa.String(length=255), nullable=True),
    sa.Column('position', sa.String(length=255), nullable=True),
    sa.Column('duties', sa.String(length=2000), nullable=True),
    sa.Column('earning', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employees_earning'), 'employees', ['earning'], unique=False)
    op.create_index(op.f('ix_employees_name'), 'employees', ['name'], unique=False)
    op.create_index(op.f('ix_employees_phoneno'), 'employees', ['phoneno'], unique=True)
    op.create_index(op.f('ix_employees_position'), 'employees', ['position'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employees_position'), table_name='employees')
    op.drop_index(op.f('ix_employees_phoneno'), table_name='employees')
    op.drop_index(op.f('ix_employees_name'), table_name='employees')
    op.drop_index(op.f('ix_employees_earning'), table_name='employees')
    op.drop_table('employees')
    # ### end Alembic commands ###