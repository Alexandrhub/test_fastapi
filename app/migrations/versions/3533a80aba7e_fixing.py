"""Fixing

Revision ID: 3533a80aba7e
Revises: 07a19041922d
Create Date: 2023-07-04 23:56:38.004066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3533a80aba7e'
down_revision = '07a19041922d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookings', 'date_from',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('bookings', 'date_to',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('bookings', 'price',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookings', 'price',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('bookings', 'date_to',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('bookings', 'date_from',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###
