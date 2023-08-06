import random
import time
import datetime

from spintop.models import SpintopTreeTestRecordBuilder
from spintop.utils import utcnow_aware
from .base import Generator

def normal(mu, sigma):
    return random.normalvariate(mu, sigma)

def random_failure(failure_odd):
    return random.uniform(0, 1.0) < failure_odd

base_mu_gen = lambda index: 5+(index*0.25)
base_sigma_gen = lambda index: 2
test_name_gen = lambda index: 'basicgen_test'
dut_id_gen = lambda index: 'dut%d' % ((index%25) if 17 < (index%25) < 20 else index % 17)
duration_gen = lambda index: 1 if (index%25) == 10 or (index%25) == 17 else 0.2


class RandomTestGenerator(Generator):
    def __call__(self, count=25, start_datetime=None, test_phases=('phase1', 'phase2'), measures=(), failure_rate=0.1):
        
        if start_datetime is None:
            start_datetime = utcnow_aware()
            
        for index in range(count):
            builder = SpintopTreeTestRecordBuilder()
            duration = duration_gen(index)
            fails = random_failure(failure_rate)
            builder.set_top_level_information(
                start_datetime=start_datetime,
                dut_id=dut_id_gen(index),
                testbench_name=test_name_gen(index),
                duration=duration,
                outcome=dict(
                    is_pass=not fails
                )
            )
            for test_name in test_phases:
                builder.new_phase(test_name, not fails, duration=duration/2)

            for measure_name in measures:
                builder.new_measure(measure_name, True, random.random())

            start_datetime += datetime.timedelta(seconds=duration)
            yield builder.build()