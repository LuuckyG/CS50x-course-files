"""user table

Revision ID: 799d80203bd7
Revises: 6a37ce5b3c31
Create Date: 2020-05-26 16:32:37.422048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '799d80203bd7'
down_revision = '6a37ce5b3c31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('bio', sa.TEXT(), nullable=True))
    op.add_column('user', sa.Column('first_name', sa.String(length=30), nullable=False))
    op.add_column('user', sa.Column('last_name', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'bio')
    # ### end Alembic commands ###
