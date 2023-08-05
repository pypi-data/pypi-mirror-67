//------------------------------------------------------------------------------
// Author: Lukasz Janyst <lukasz@jany.st>
// Date: 21.02.2018
//
// Licensed under the 3-Clause BSD License, see the LICENSE file for details.
//------------------------------------------------------------------------------

export const JOB_LIST_SET = 'JOB_LIST_SET';
export const JOB_UPDATE = 'JOB_UPDATE';
export const JOB_REMOVE = 'JOB_REMOVE';

export function jobListSet(status, jobs) {
  return {
    type: JOB_LIST_SET,
    status,
    jobs
  };
}

export function jobUpdate(job) {
  return {
    type: JOB_UPDATE,
    job
  };
}

export function jobRemove(jobId) {
  return {
    type: JOB_REMOVE,
    jobId
  };
}
