"""add content column to posts

Revision ID: 102148d97955
Revises: 043c2276375a
Create Date: 2025-09-02 11:41:50.605902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '102148d97955'
down_revision = '043c2276375a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    pass
