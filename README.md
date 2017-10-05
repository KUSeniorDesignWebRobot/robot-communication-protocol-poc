# Robot Communication Protocol POC

Proof of concept for robot communication protocol

Message handlers on both ends should be tolerant of extraneous fields but intolerant of missing or malformed fields

If multiple command or report messages would be sent at the same time, they may be merged into a single message with a list of individual values, ttl, and relevant metadata.