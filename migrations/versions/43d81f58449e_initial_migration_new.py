"""initial_migration_new

Revision ID: 43d81f58449e
Revises: 
Create Date: 2025-04-29 19:26:25.959865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43d81f58449e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('hashed_password', sa.String(length=128), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('note',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('note_belongs_to_tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('note_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['note_id'], ['note.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notification',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('is_read', sa.Boolean(), nullable=True),
    sa.Column('note_id', sa.Integer(), nullable=True),
    sa.Column('referenced_user_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['note_id'], ['note.id'], ),
    sa.ForeignKeyConstraint(['referenced_user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_has_access_note',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('note_id', sa.Integer(), nullable=True),
    sa.Column('shared_by', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['note_id'], ['note.id'], ),
    sa.ForeignKeyConstraint(['shared_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_has_access_note')
    op.drop_table('notification')
    op.drop_table('note_belongs_to_tag')
    op.drop_table('tag')
    op.drop_table('note')
    op.drop_table('user')
    # ### end Alembic commands ###
