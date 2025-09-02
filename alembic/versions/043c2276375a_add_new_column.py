"""add new column

Revision ID: 043c2276375a
Revises: 
Create Date: 2025-09-02 11:34:03.367622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '043c2276375a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False, primary_key=True),
                    sa.Column('title',sa.String(),nullable=False
                    ))

def downgrade() -> None:
    """Downgrade schema."""
    pass
