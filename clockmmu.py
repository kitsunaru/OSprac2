from mmu import MMU

class ClockMMU(MMU):
    def __init__(self, frames):
        # TODO: Constructor logic for clockMMU
        self.clock_index = 0
        self.clock_mem_table = [None] * (frames)
        self.use_arr = [None] * (frames)
        self.clock_frames = frames
        self.dirty_arr = []
        self.read_count = 0
        self.write_count = 0
        self.fault_count = 0
        self.dbg = None

    def ClockWork(self):
        pass

    def set_debug(self):
        # TODO: Implement the method to set debug mode
        self.dbg = True

    def reset_debug(self):
        # TODO: Implement the method to reset debug mode
        self.dbg = False

    def read_memory(self, page_number):
        # TODO: Implement the method to read memory

        # TODO: add a check with empty page, and adding handler for there is an empty page
        if page_number not in self.clock_mem_table:
            self.fault_count += 1
            self.read_count += 1
            
            if None not in self.clock_mem_table:
                while self.use_arr[self.clock_index] == 1:
                    self.use_arr[self.clock_index] = 0
                    self.clock_index += 1
                    self.clock_index %= self.clock_frames

                if self.clock_mem_table[self.clock_index] in self.dirty_arr:
                    self.write_count += 1
                    self.dirty_arr.remove(self.clock_mem_table[self.clock_index])

                    if self.dbg:
                        print("--------------------------------")
                        print("######")
                        print(f"Evict victim: page number: {self.clock_mem_table[self.clock_index]}")
                        print("######")
            else:
                for i in range(self.clock_frames):
                    if self.clock_mem_table[i] == None:
                        self.clock_index = i
                        break
            self.use_arr[self.clock_index] = 1


            self.clock_mem_table[self.clock_index] = page_number
            if self.dbg:
                # print("--------------------------------")
                print("Page Fault")
                print(f"Read from disk: {page_number}")
            # if page_number in self.dirty_arr:
                # self.dirty_arr.remove(page_number)
        else:
            for i in range(self.clock_frames):
                if self.clock_mem_table[i] == page_number:
                    self.use_arr[i] = 1

            if self.dbg:
                # print("--------------------------------")
                print(f"Read from memory: {page_number}")
        if self.dbg:
                print(f"Dirty: {self.dirty_arr}")
                print(f"stuff in memory: {self.clock_mem_table}")

    def write_memory(self, page_number):
        # TODO: Implement the method to write memory

        if page_number not in self.clock_mem_table:
            self.fault_count += 1
            self.read_count += 1
            if self.dbg:
                print("--------------------------------")
                print("Page Fault")

            if None not in self.clock_mem_table:
                while self.use_arr[self.clock_index] == 1:
                    self.use_arr[self.clock_index] = 0
                    self.clock_index += 1
                    self.clock_index %= self.clock_frames

                if self.clock_mem_table[self.clock_index] in self.dirty_arr:
                    self.write_count += 1
                    self.dirty_arr.remove(self.clock_mem_table[self.clock_index])
                    if self.dbg:
                        print(f"Disk Write: {self.clock_mem_table[0]}")
                        print(f"stuff in memory: {self.clock_mem_table}")
            else:
                for i in range(self.clock_frames):
                    if self.clock_mem_table[i] == None:
                        self.clock_index = i
                        break
            self.use_arr[self.clock_index] = 1

                

            if self.dbg:
                if self.clock_mem_table[self.clock_index] is not None:
                    print(f"Write: {self.clock_mem_table[self.clock_index]}")
                print(f"Evict victim: page number: {self.clock_mem_table[self.clock_index]}")
            self.clock_mem_table[self.clock_index] = page_number

            if page_number not in self.dirty_arr:
                self.dirty_arr.append(page_number)
            if self.dbg:
                print(f"mem: {self.clock_mem_table}")
                print(f"dirty pile: {self.dirty_arr}")
        else:
            if self.dbg:
                print(f"In MMU Write: {page_number}")
            for i in range(self.clock_frames):
                if self.clock_mem_table[i] == page_number:
                    self.use_arr[i] = 1
                    break
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
