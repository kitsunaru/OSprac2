from mmu import MMU
from random import randint

class RandMMU(MMU):
    def __init__(self, frames):
        # TODO: Constructor logic for LruMMU
        self.rand_mem_table = [None] * (frames)
        self.rand_frame = frames
        self.evict = 0
        self.dirty_arr = []
        self.read_count = 0
        self.write_count = 0
        self.fault_count = 0
        self.dbg = None

    def set_debug(self):
        # TODO: Implement the method to set debug mode
        self.dbg = True

    def reset_debug(self):
        # TODO: Implement the method to reset debug mode
        self.dbg = False

    def read_memory(self, page_number):
        self.evict = randint(0, (self.rand_frame - 1))

        if None not in self.rand_mem_table:
            if page_number not in self.rand_mem_table:
                self.fault_count += 1
                self.read_count += 1

                if self.rand_mem_table[self.evict] in self.dirty_arr:
                    self.write_count += 1
                    self.dirty_arr.remove(self.rand_mem_table[self.evict])
                if self.dbg:
                    print("--------------------------------")
                    print("######")
                    print(f"Evict victim frame number: {self.evict}")
                    print("######")
                self.rand_mem_table.pop(self.evict)
                self.rand_mem_table.append(page_number)

                if page_number in self.dirty_arr:
                    self.dirty_arr.remove(page_number)
            else:
                self.rand_mem_table.remove(page_number)
                self.rand_mem_table.append(page_number)
        else:
            for i in range(self.rand_frame):
                if self.rand_mem_table[i] == None:
                    self.rand_mem_table[i] = page_number
                    break
            if self.dbg:
                    print("--------------------------------")
                    print("######")
                    print(f"With empty frame evict victim frame number: {self.evict}")
                    print("######")
                    print(f"Stuff in memory: {self.rand_mem_table}")


    def write_memory(self, page_number):
        # TODO: Implement the method to write memory
        self.evict = randint(0, (self.rand_frame - 1))

        if None not in self.rand_mem_table:
            if page_number not in self.rand_mem_table:
                self.fault_count += 1
                self.read_count += 1
                
                if self.rand_mem_table[self.evict] in self.dirty_arr:
                    self.dirty_arr.remove(self.rand_mem_table[self.evict])
                    self.write_count += 1

                if self.dbg:
                    if self.rand_mem_table[self.evict] is not None:
                        print(f"Write: {self.rand_mem_table[self.evict]}")
                    print(f"Evict victim frame number: {self.evict}")
                self.rand_mem_table.pop(self.evict)
                self.rand_mem_table.append(page_number)

                if page_number not in self.dirty_arr:
                    self.dirty_arr.append(page_number)
            else:
                self.rand_mem_table.remove(page_number)
                self.rand_mem_table.append(page_number)
                if page_number not in self.dirty_arr:
                    self.dirty_arr.append(page_number)
        else:
            for i in range(self.rand_frame):
                if self.rand_mem_table[i] == None:
                    self.rand_mem_table[i] = page_number
                    if page_number not in self.dirty_arr:
                        self.dirty_arr.append(page_number)
                    break
            if self.dbg:
                    print("--------------------------------")
                    print("######")
                    print(f"With empty frame evict victim frame number: {self.evict}")
                    print("######")
                    print(f"Stuff in memory: {self.rand_mem_table}")

    def get_total_disk_reads(self):
        # TODO: Implement the method to get total disk reads
        return self.read_count

    def get_total_disk_writes(self):
        # TODO: Implement the method to get total disk writes
        return self.write_count

    def get_total_page_faults(self):
        # TODO: Implement the method to get total page faults
        return self.fault_count
