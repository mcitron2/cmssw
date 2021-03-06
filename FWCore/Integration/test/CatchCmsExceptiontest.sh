#!/bin/sh

# Pass in name and status
function die { echo $1: status $2 ;  exit $2; }

pushd ${LOCAL_TMP_DIR}

cmsRun ${LOCAL_TEST_DIR}/CatchCmsExceptiontest_cfg.py &> CatchCmsException.log && die 'Failed in using CatchCmsException_cfg.py' $? 

grep -q WhatsItESProducer CatchCmsException.log || die 'Failed to find Producers name' $?

echo running cmsRun testSkipEvent_cfg.py
cmsRun ${LOCAL_TEST_DIR}/testSkipEvent_cfg.py &> testSkipEvent.log || die 'Failed in using testSkipEvent_cfg.py' $? 

popd

#grep -w ESProducer CatcheStdException.log
