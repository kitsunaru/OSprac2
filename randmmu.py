from mmu import MMU
from random import randint

class RandMMU(MMU):
    def __init__(self, frames):
        # TODO: Constructor logic for RandMMU
        self.rand_mem_table = [None] * (frames)
        self.dirty_arr = []
        self.disk_arr = []
        self.read_count = 0
        self.write_count = 0
        self.fault_count = 0
        self.dbg = None

    def set_debug(self):
        # TODO: Implement the method to set debug mode
        self.dbg = True # sets the debug mode to True

    def reset_debug(self):
        # TODO: Implement the method to reset debug mode
        self.dbg = False # resets the debug mode to False

    def read_memory(self, page_number):
        # TODO: Implement the method to read memory
        # randint()
        
        pass

    def write_memory(self, page_number):
        # TODO: Implement the method to write memory
        # take the randint() result from read_memory
        pass

    def get_total_disk_reads(self):
        # TODO: Implement the method to get total disk reads
        return -1

    def get_total_disk_writes(self):
        # TODO: Implement the method to get total disk writes
        return -1

    def get_total_page_faults(self):
        # TODO: Implement the method to get total page faults
        return -1
