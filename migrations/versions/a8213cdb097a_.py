"""empty message

Revision ID: a8213cdb097a
Revises: 87301ed2adb3
Create Date: 2021-06-23 14:32:21.911752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8213cdb097a'
down_revision = '87301ed2adb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Outgate', 'tarewbid')
    op.add_column('blacklist_tokens', sa.Column('userid', sa.Integer(), autoincrement=True, nullable=False))
    op.drop_column('blacklist_tokens', 'user_id')
    op.drop_column('vehicles', 'vownership')
    op.drop_column('vehicles', 'vaddress')
    op.drop_column('vehicles', 'vowner')
    op.drop_column('vehicles', 'vcontact')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vehicles', sa.Column('vcontact', sa.VARCHAR(length=50), nullable=True))
    op.add_column('vehicles', sa.Column('vowner', sa.VARCHAR(length=50), nullable=True))
    op.add_column('vehicles', sa.Column('vaddress', sa.VARCHAR(length=50), nullable=True))
    op.add_column('vehicles', sa.Column('vownership', sa.BOOLEAN(), server_default=sa.text("'false'"), nullable=True))
    op.add_column('blacklist_tokens', sa.Column('user_id', sa.INTEGER(), nullable=False))
    op.drop_column('blacklist_tokens', 'userid')
    op.add_column('Outgate', sa.Column('tarewbid', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
