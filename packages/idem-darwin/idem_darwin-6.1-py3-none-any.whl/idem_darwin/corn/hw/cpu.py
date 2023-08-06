import shutil


async def load_num_cpus(hub):
    sysctl = shutil.which("sysctl")
    if sysctl:
        hub.corn.CORN.num_cpus = int(
            (await hub.exec.cmd.run([sysctl, "-n", "hw.ncpu"])).stdout.strip()
        )


async def load_cpu_arch(hub):
    sysctl = shutil.which("sysctl")
    if sysctl:
        hub.corn.CORN.cpuarch = (
            await hub.exec.cmd.run([sysctl, "-n", "hw.machine"])
        ).stdout.strip()


async def load_cpu_model(hub):
    sysctl = shutil.which("sysctl")
    if sysctl:
        hub.corn.CORN.cpu_model = (
            await hub.exec.cmd.run([sysctl, "-n", "machdep.cpu.brand_string"])
        ).stdout


async def load_cpu_flags(hub):
    sysctl = shutil.which("sysctl")
    if sysctl:
        hub.corn.CORN.cpu_flags = sorted(
            (await hub.exec.cmd.run([sysctl, "-n", "machdep.cpu.features"]))
            .stdout.strip()
            .lower()
            .split(" ")
        )

        # Report if hardware virtualization is available under amd or intel
        hub.corn.CORN.hardware_virtualization = bool(
            {"svm", "vmx"} - set(hub.corn.CORN.cpu_flags)
        )
