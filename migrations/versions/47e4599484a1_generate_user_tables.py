"""generate_user_tables

Revision ID: 47e4599484a1
Revises: 89edb69f4be3
Create Date: 2018-05-10 21:33:01.943092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47e4599484a1'
down_revision = '89edb69f4be3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sp_users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('sp_users', sa.Column('password', sa.String(length=255), nullable=True))
    op.add_column('sp_users', sa.Column('registration_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sp_users', 'registration_at')
    op.drop_column('sp_users', 'password')
    op.drop_column('sp_users', 'email')
    # ### end Alembic commands ###
