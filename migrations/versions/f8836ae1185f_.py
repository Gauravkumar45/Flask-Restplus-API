"""empty message

Revision ID: f8836ae1185f
Revises: 39ece19f5a5d
Create Date: 2021-05-20 22:25:06.340150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8836ae1185f'
down_revision = '39ece19f5a5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('token'),
    sa.UniqueConstraint('token')
    )
    op.create_table('drivers',
    sa.Column('driverid', sa.Integer(), nullable=False),
    sa.Column('drivername', sa.String(length=50), nullable=True),
    sa.Column('dlno', sa.String(length=50), nullable=True),
    sa.Column('dltype', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('dlexpiry', sa.DateTime(), nullable=True),
    sa.Column('isactive', sa.Boolean(), server_default='true', nullable=True),
    sa.Column('drivermobile', sa.String(length=50), nullable=True),
    sa.Column('fingerprint', sa.String(length=50), nullable=True),
    sa.Column('faceprint', sa.String(length=50), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.Column('statuschangedate', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('driverid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('drivers')
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
