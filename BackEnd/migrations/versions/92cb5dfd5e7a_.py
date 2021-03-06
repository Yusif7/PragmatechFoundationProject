"""empty message

Revision ID: 92cb5dfd5e7a
Revises: 
Create Date: 2021-02-04 13:40:42.620005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92cb5dfd5e7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('blog_info', sa.String(length=50), nullable=False))
    op.alter_column('category', 'category_all',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)
    op.add_column('works', sa.Column('categoryId', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'works', 'category', ['categoryId'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'works', type_='foreignkey')
    op.drop_column('works', 'categoryId')
    op.alter_column('category', 'category_all',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
    op.drop_column('blog', 'blog_info')
    # ### end Alembic commands ###
