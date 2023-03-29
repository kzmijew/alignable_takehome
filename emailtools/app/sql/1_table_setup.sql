-- Set up schema
CREATE SCHEMA IF NOT EXISTS alignable;
SET search_path TO alignable;

-- Set up enums 
CREATE TYPE mailer_types AS ENUM ('Notification');
CREATE TYPE notification_types AS ENUM ('connection_request', 'received_recommendation');
CREATE TYPE email_events AS ENUM ('clicked', 'opened');
CREATE TYPE session_events_enum AS ENUM ('connection_request_accepted', 'recommendation_request_accepted', 'connection_request_sent', 'conversation_message', 'recommendation_request_sent')

-- Set up tables
CREATE TABLE IF NOT EXISTS mailings (
    mailing_id integer primary key,
    mailer mailer_types,
    action notification_types,
    mailing_on date
);

CREATE TABLE IF NOT EXISTS sent_emails (
    sent_email_id bigint primary key,
    mailing_id integer references mailings(mailing_id)
);

CREATE TABLE IF NOT EXISTS sent_email_events (
    sent_email_id bigint references sent_emails(sent_email_id),
    event_name email_events,
    properties jsonb
);

CREATE TABLE IF NOT EXISTS sessions (
    session_id uuid primary key,
    tracking_id uuid
);

CREATE TABLE IF NOT EXISTS session_events (
    session_id uuid references sessions(session_id),
    event_name session_events_enum
);



