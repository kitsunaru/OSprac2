from mmu import MMU
from random import randint

class RandMMU(MMU):
    def __init__(self, frames):
        # TODO: Constructor logic for RandMMU
        self.rand_mem_table = [None] * (frames)
        self.dirty_arr = []
        self.read_count = 0
        self.write_count = 0
        self.fault_count = 0
        self.dbg = None

    def set_debug(self):
        # TODO: Implement the method to set debug mode
        self.dbg = True # switch the debug mode to True when function is called

    def reset_debug(self):
        # TODO: Implement the method to reset debug mode
        self.dbg = False # reset debug mode to False when function is called

    def read_memory(self, page_number):
        # TODO: Implement the method to read memory

        # TODO: add a check with empty page, and adding handler for there is an empty page
        rand_gen = random.randint(0, (frames-1))
        if page_number not in self.rand_mem_table:
            self.fault_count += 1
            self.read_count += 1
            # if None not in self.rand_mem_table:

            # TODO: add element 0 dirty bit check, if it is dirty -> write to disk (w_cnt++); then pop element 0
            if self.rand_mem_table[rand_gen] in self.dirty_arr:
                self.write_count += 1
                self.dirty_arr.remove(self.rand_mem_table[rand_gen])
            if self.dbg:
                print("--------------------------------")
                print("######")
                print(f"Evict victim: page number: {self.rand_mem_table[rand_gen]}")
                print("######")
            self.rand_mem_table.pop(rand_gen)
            self.rand_mem_table.append(page_number)
            if self.dbg:
                # print("--------------------------------")
                print("Page Fault")
                print(f"Read from disk: {page_number}")
            if page_number in self.dirty_arr:
                self.dirty_arr.remove(page_number)
        else:
            self.rand_mem_table.remove(page_number)
            self.rand_mem_table.append(page_number)
            if self.dbg:
                # print("--------------------------------")
                print(f"Read from memory: {page_number}")
        if self.dbg:
                print(f"Dirty: {self.dirty_arr}")
                print(f"stuff in memory: {self.rand_mem_table}")

    def write_memory(self, page_number):
        # TODO: Implement the method to write memory
        rand_gen = random.randint(0, (frames-1))
        if page_number not in self.rand_mem_table:
            self.fault_count += 1
            self.read_count += 1
            if self.dbg:
                print("--------------------------------")
                print("Page Fault")

            if self.rand_mem_table[rand_gen] in self.dirty_arr:
                self.dirty_arr.remove(self.rand_mem_table[rand_gen])
                self.write_count += 1
                if self.dbg:
                    print(f"Disk Write: {self.rand_mem_table[rand_gen]}")
                    print(f"stuff in memory: {self.rand_mem_table}")

            if self.dbg:
                if self.rand_mem_table[0] is not None:
                    print(f"Write: {self.rand_mem_table[rand_gen]}")
                print(f"Evict victim: page number: {self.rand_mem_table[rand_gen]}")
            self.rand_mem_table.pop(rand_gen)
            self.rand_mem_table.append(page_number)

            if page_number not in self.dirty_arr:
                self.dirty_arr.append(page_number)
            if self.dbg:
                print(f"mem: {self.rand_mem_table}")
                print(f"dirty pile: {self.dirty_arr}")
        else:
            if self.dbg:
                print(f"In MMU Write: {page_number}")
            self.rand_mem_table.remove(page_number)
            self.rand_mem_table.append(page_number)
            if page_number not in self.dirty_arr:
                self.dirty_arr.append(page_number)

    def get_total_disk_reads(self):
        # TODO: Implement the method to get total disk reads
        return self.read_count

    def get_total_disk_writes(self):
        # TODO: Implement the method to get total disk writes
        return self.write_count

    def get_total_page_faults(self):
        # TODO: Implement the method to get total page faults
        return self.fault_count
