# Robot Communication Protocol POC

Proof of concept for robot communication protocol

Message handlers on both ends should be tolerant of extraneous fields but intolerant of missing or malformed fields

If multiple command or report messages would be sent at the same time, they may be merged into a single message with a list of individual values, ttl, and relevant metadata.

# ZMQ Server-Client POC

Along with the language of the robot communication protocol, a proof of concept of multi-client encrypted communication is provided in the example_zmq_python/TCP_Encrypted_REQREP_multi_client folder.

These Python scripts demonstrate how to run multiple encrypted clients communicating with one endpoint.  To run this demonstration, run the ser.py Python script first, and then run one or both of the client scripts.  The communication is encrypted and both of the clients run by attaching to only one port.