"""add patient and healthprofessional tables

Revision ID: bb120caca4a5
Revises: 26e8da5548b5
Create Date: 2024-03-04 23:53:30.036496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb120caca4a5'
down_revision = '26e8da5548b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('health_professionals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('medical_register', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('weight', sa.Numeric(precision=5, scale=2), nullable=False),
    sa.Column('race', sa.String(length=20), nullable=False),
    sa.Column('height', sa.Numeric(precision=5, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(length=80), nullable=False))

    op.drop_table('patients')
    op.drop_table('health_professionals')
    # ### end Alembic commands ###
