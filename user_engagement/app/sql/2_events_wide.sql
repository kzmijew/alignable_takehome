SET search_path = alignable;

-- join all tables to create wide view
CREATE TABLE email_events_full_context AS 
WITH events_wide AS (
    SELECT 
        sent_email_id,
        event_name,
        properties->>'device_name' AS device_name,
        properties->>'tracking_id' AS tracking_id,
        properties->>'browser_name' AS browser_name,
        properties->>'platform_name' AS platform_name,
        properties->>'browser_version' AS browser_version,
        properties->>'platform_version' AS platform_version
    FROM sent_email_events 
)
SELECT
    sent_emails.*,
    mailings.mailer,
    mailings.action,
    mailings.mailing_on,
    events_wide.event_name,
    events_wide.device_name,
    events_wide.tracking_id,
    events_wide.browser_name,
    events_wide.platform_name,
    events_wide.browser_version,
    events_wide.platform_version,
    sessions.session_id,
    session_events.event_name as session_event_name
FROM sent_emails
LEFT JOIN mailings ON sent_emails.mailing_id = mailings.mailing_id
LEFT JOIN events_wide ON sent_emails.sent_email_id = events_wide.sent_email_id
LEFT JOIN sessions ON events_wide.tracking_id::uuid = sessions.tracking_id
LEFT JOIN session_events ON session_events.session_id = sessions.session_id