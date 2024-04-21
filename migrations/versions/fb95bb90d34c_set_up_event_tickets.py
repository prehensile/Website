"""set up event tickets

Revision ID: fb95bb90d34c
Revises: e9529c62ca57
Create Date: 2024-04-27 23:41:01.799894

"""

# revision identifiers, used by Alembic.
revision = 'fb95bb90d34c'
down_revision = '56f4836885de'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_ticket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('proposal_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('rank', sa.Integer(), nullable=True),
    sa.Column('ticket_count', sa.Integer(), nullable=True),
    sa.Column('ticket_codes', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposal.id'], name=op.f('fk_event_ticket_proposal_id_proposal')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_event_ticket_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_event_ticket'))
    )
    op.add_column('proposal', sa.Column('requires_ticket', sa.Boolean(), nullable=True))
    op.add_column('proposal', sa.Column('total_tickets', sa.Integer(), nullable=True))
    op.add_column('proposal', sa.Column('non_lottery_tickets', sa.Integer(), nullable=True))
    op.add_column('proposal_version', sa.Column('requires_ticket', sa.Boolean(), autoincrement=False, nullable=True))
    op.add_column('proposal_version', sa.Column('total_tickets', sa.Integer(), autoincrement=False, nullable=True))
    op.add_column('proposal_version', sa.Column('non_lottery_tickets', sa.Integer(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('proposal_version', 'non_lottery_tickets')
    op.drop_column('proposal_version', 'total_tickets')
    op.drop_column('proposal_version', 'requires_ticket')
    op.drop_column('proposal', 'non_lottery_tickets')
    op.drop_column('proposal', 'total_tickets')
    op.drop_column('proposal', 'requires_ticket')
    op.drop_table('event_ticket')
    # ### end Alembic commands ###
