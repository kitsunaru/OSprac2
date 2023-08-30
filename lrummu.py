from mmu import MMU

class LruMMU(MMU):
    def __init__(self, frames):
        # TODO: Constructor logic for LruMMU
        self.lru_mem_table = [None] * (frames - 1)
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
        # TODO: Implement the method to read memory
        if page_number not in self.lru_mem_table:
            self.fault_count += 1
            if self.dbg:
                print("Page Fault")
                print("Read")
                print(f"Evict victim: page number: {self.lru_mem_table[0]}")
                print(f"stuff in memory: {self.lru_mem_table}")
            self.lru_mem_table.pop(0)
            self.lru_mem_table.append(page_number)
        else:
            self.dirty_arr.append(page_number)
        self.read_count += 1

    def write_memory(self, page_number):
        # TODO: Implement the method to write memory
        if page_number not in self.lru_mem_table:
            self.fault_count += 1
            if self.dbg:
                print("Page Fault")
                print(f"stuff in memory: {self.lru_mem_table}")
            if page_number in self.dirty_arr:
                self.dirty_arr.remove(page_number)
                self.write_count += 1
                if self.dbg:
                    print("Disk Write")
                    print(f"stuff in memory: {self.lru_mem_table}")
            else:
                print("Write")
                if None not in self.lru_mem_table:
                    if self.dbg:
                        print(f"Evict victim: page number: {self.lru_mem_table[0]}")
                        print(f"stuff in memory: {self.lru_mem_table}")
                    self.lru_mem_table.pop(0)
                self.lru_mem_table.append(page_number)
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
