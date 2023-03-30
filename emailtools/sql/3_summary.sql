CREATE TABLE alignable.email_stats AS
SELECT 
    mailing_id, 
    mailer, 
    action,
    event_name,
    session_event_name,
    count(DISTINCT sent_email_id) as count
FROM alignable.email_events_full_context
GROUP BY 1,2,3,4,5;

