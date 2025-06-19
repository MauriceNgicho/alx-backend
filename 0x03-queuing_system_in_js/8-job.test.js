import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

// Enable Kue test mode that will not process data
const queue = kue.createQueue({});

describe('createPushNotificationsJobs', () => {
  before(() => {
    kue.Job.rangeByType('push_notification_code_3', 'inactive', 0, -1, 'asc', (err, selectedJobs) => {
      selectedJobs.forEach(job => job.remove());
    });
  });

  beforeEach(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();  // Clear all test jobs
    queue.testMode.exit();   // Exit test mode
  });

  it('should display an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not-an-array', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Hello job 1' },
      { phoneNumber: '0987654321', message: 'Hello job 2' }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Test that 2 jobs were created
    expect(queue.testMode.jobs.length).to.equal(2);

    // Test job data for job 1
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);

    // Test job type
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
  });
});
