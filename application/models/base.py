# coding=utf-8
import sqlalchemy as sa
from sqlalchemy import Column


class BaseModelMixin(object):
    created_at = Column(sa.DateTime, server_default=sa.text('current_timestamp()'), index=True)
    updated_at = Column(
        sa.DateTime,
        onupdate=sa.text('current_timestamp()'),
        server_default=sa.text('current_timestamp()'),
        index=True,
    )
