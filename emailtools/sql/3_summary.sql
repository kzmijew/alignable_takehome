CREATE TABLE alignable.email_campaign_engagement AS
WITH sends AS (
    SELECT mailing_id, mailer, action, count(DISTINCT sent_email_id) as sends 
    FROM alignable.email_events_full_context GROUP BY 1,2,3
), opens AS (
    SELECT mailing_id, mailer, action, event_name, count(DISTINCT sent_email_id) as opens
    FROM alignable.email_events_full_context 
    WHERE event_name = 'opened'
    GROUP BY 1,2,3,4
), clicks AS (
    SELECT mailing_id, mailer, action, event_name, count(DISTINCT sent_email_id) as clicks
    FROM alignable.email_events_full_context 
    WHERE event_name = 'clicked'
    GROUP BY 1,2,3,4
), connection_requests_accepted AS (
    -- NOTE: this assumes each row in session_events.csv is valid and may overcount if not the case
    SELECT mailing_id, session_event_name, 
    SUM(events_count) AS connection_requests_accepted,
    count(DISTINCT session_id) AS connection_requests_accepted_by_session
    FROM alignable.email_events_full_context
    WHERE event_name = 'clicked'
    AND session_event_name = 'connection_request_accepted'
    GROUP BY 1,2
), connection_requests_sent AS (
    SELECT mailing_id, session_event_name, SUM(events_count) AS connection_requests_sent,
    count(DISTINCT session_id) AS connection_requests_sent_by_session
    FROM alignable.email_events_full_context
    WHERE event_name = 'clicked'
    AND session_event_name = 'connection_request_sent'
    GROUP BY 1,2
), recommendations_accepted AS (
    SELECT mailing_id, session_event_name, SUM(events_count) AS recommendations_accepted,
    count(DISTINCT session_id) AS recommendations_accepted_by_session
    FROM alignable.email_events_full_context
    WHERE event_name = 'clicked'
    AND session_event_name = 'recommendation_request_accepted'
    GROUP BY 1,2
), recommendations_sent AS (
    SELECT mailing_id, session_event_name, SUM(events_count) AS recommendations_sent,
    count(DISTINCT session_id) AS recommendations_sent_by_session
    FROM alignable.email_events_full_context
    WHERE event_name = 'clicked'
    AND session_event_name = 'recommendation_request_sent'
    GROUP BY 1,2
), conversation_messages_sent AS (
    SELECT mailing_id, session_event_name, SUM(events_count) AS conversation_messages_sent,
    count(DISTINCT session_id) AS conversation_messages_sent_by_session
    FROM alignable.email_events_full_context
    WHERE event_name = 'clicked'
    AND session_event_name = 'conversation_message'
    GROUP BY 1,2
)
SELECT 
    sends.*,
    opens.opens,
    clicks.clicks,
    connection_requests_accepted.connection_requests_accepted,
    connection_requests_accepted.connection_requests_accepted_by_session,
    connection_requests_sent.connection_requests_sent,
    connection_requests_sent.connection_requests_sent_by_session,
    recommendations_accepted.recommendations_accepted,
    recommendations_accepted.recommendations_accepted_by_session,
    recommendations_sent.recommendations_sent,
    recommendations_sent.recommendations_sent_by_session,
    conversation_messages_sent.conversation_messages_sent,
    conversation_messages_sent.conversation_messages_sent_by_session
FROM sends 
LEFT JOIN opens ON (sends.mailing_id = opens.mailing_id)
LEFT JOIN clicks ON (sends.mailing_id = clicks.mailing_id)
LEFT JOIN connection_requests_accepted ON (sends.mailing_id = connection_requests_accepted.mailing_id)
LEFT JOIN connection_requests_sent ON (sends.mailing_id = connection_requests_sent.mailing_id)
LEFT JOIN recommendations_accepted ON (sends.mailing_id = recommendations_accepted.mailing_id)
LEFT JOIN recommendations_sent ON (sends.mailing_id = recommendations_sent.mailing_id)
LEFT JOIN conversation_messages_sent ON (sends.mailing_id = conversation_messages_sent.mailing_id)

