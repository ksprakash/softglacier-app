# import logging
# from watchtower import CloudWatchLogHandler
# def logger(app,log_group_name,log_stream_name,boto3_profile_name):
#     formatter='%(asctime)s - %(levelname)s - %(message)s'
#     logging.basicConfig(level=logging.DEBUG,format=formatter)
#     handler = CloudWatchLogHandler(log_group_name=log_group_name,log_stream_name=log_stream_name,boto3_profile_name=boto3_profile_name)
#     app.logger.addHandler(handler)
#     logging.getLogger().addHandler(handler)
#     return logging
    

#Basic Config for Console

# import logging and sys package
# import logging
# import sys
# create logger first
# logger = logging.getLogger()
# set level ogf logger
# logger.setLevel(logging.DEBUG)
# create stream handler
# streamhdlr = logging.StreamHandler(sys.stderr)
# add stream handler to logger
# logger.addHandler(streamhdlr)
# set level of stream handler
# streamhdlr.setLevel(logging.DEBUG)
# logger.info(" we use sys.stderr as stream ")
# we can set stream by setStream handler method
# streamhdlr.setStream(sys.stdout)
# logger.info('now we use sys.stdout as stream')