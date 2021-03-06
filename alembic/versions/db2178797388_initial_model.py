"""Initial model

Revision ID: db2178797388
Revises: 
Create Date: 2021-12-08 14:23:47.864621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db2178797388'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_site', sa.String(), nullable=True),
    sa.Column('url_site', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('profile_picture', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('google_sheet',
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('id_site', sa.Integer(), nullable=False),
    sa.Column('url_sheet', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id_site'], ['site.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id_user', 'id_site')
    )
    op.create_table('raffle',
    sa.Column('id_site', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('url_raffle', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id_site'], ['site.id'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id_site', 'id_user')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('raffle')
    op.drop_table('google_sheet')
    op.drop_table('user')
    op.drop_table('site')
    # ### end Alembic commands ###
